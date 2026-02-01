---
title:  "Virtualization Nightmare: Multipass in VirtualBox"
date:   2025-04-18 10:00:00 +0800
tags: [Programming]
---

So, I recently embarked on a virtualization adventure that quickly turned into a troubleshooting marathon. Let me preface this by saying I'm a fan of experimentation, but sometimes, that experimentation leads you down a rabbit hole filled with ACPI errors, Grub rescue prompts, and the distinct smell of burning silicon (okay, maybe not the last one, but it *felt* like it).

**The Original (Failed) Plan: VirtualBox Inception**

My goal was simple: to run `multipass` inside a virtual machine. Why?  Let's just say it was for science!  My initial setup looked like this:

*   **Host OS:** Linux Mint (because I like it!)
*   **Hypervisor:** VirtualBox (because it's convenient)
*   **Guest OS:** Lubuntu (lightweight, seemed perfect)
*   **The Goal:** Run `multipass` inside the Lubuntu VM, leveraging Nested VT-x (the ability to virtualize *within* a virtual machine).

Sounds straightforward, right? Wrong.

I installed VirtualBox on my Mint host, spun up a Lubuntu VM, and then tried to enable Nested VT-x. That's where the trouble started.  Almost immediately, I ran into a cascade of errors, culminating in a corrupted Grub bootloader on my *host* machine!  Yes, you read that right. My host OS was refusing to boot. I was staring into the abyss of the dreaded Grub rescue prompt.

The culprit?  I suspect a combination of factors. Enabling Nested VT-x in VirtualBox can be finicky. It might be due to a BIOS ACPI conflict, or some other gremlin in the communication between the hypervisor and the hardware. Whatever it was, it trashed my Grub configuration.

**The (Successful) Redemption: KVM to the Rescue**

After a frantic recovery involving a live USB and some Grub surgery, I decided to take a different approach. I realized I was trying to force something that wasn't working well.  It was time to ditch VirtualBox for this particular task and embrace a more native Linux solution: KVM.

Here's the setup that *actually* worked:

*   **Host OS:** Linux Mint (still rocking it!)
*   **Hypervisor:** KVM (via `qemu/libvirt`)
*   **Guest OS:** Ubuntu Server (command line all the way!)
*   **The Goal:** Run `multipass` inside the Ubuntu Server VM, leveraging Nested VT-x.

This time, the installation was much smoother. I installed Ubuntu Server, enabled Nested VT-x for the VM in `virt-manager`, and then installed `multipass`. Everything worked!

**The Performance Difference is Real**

But the real surprise wasn't just that it worked; it was the *performance*. The KVM-based setup absolutely crushed the VirtualBox attempt.  Things felt significantly faster and more responsive.  It makes sense in retrospect.  KVM is a Type 1 hypervisor, meaning it runs directly on the hardware, giving it much better access to resources compared to VirtualBox, which is a Type 2 hypervisor running on top of the host OS.

**Key Takeaways and Lessons Learned**

*   **Nested VT-x with VirtualBox can be problematic:** Be prepared for potential headaches, especially with more complex configurations.
*   **KVM is a performance powerhouse (especially on Linux):**  If you're on Linux and need robust virtualization, KVM is often the superior choice.
*   **Simplify Your Setup:** Avoid unnecessary layers of virtualization whenever possible.
*   **Check your BIOS:** Ensure VT-x/AMD-V is enabled in your BIOS settings. Also, updating your BIOS can resolve ACPI related issues.
*   **Use Virtualization Management Tools:** Tools like `virt-manager` or `virsh` give you fine-grained control over your VMs.

**Conclusion**

This experience taught me a valuable lesson about the nuances of virtualization. While VirtualBox is a great tool, it's not always the best choice for every task, especially when you're pushing the boundaries with features like Nested VT-x. KVM provided a much more stable and performant platform for running `multipass` in a virtualized environment. Now, back to my experiments (hopefully with fewer Grub emergencies this time!).  Happy virtualizing!
