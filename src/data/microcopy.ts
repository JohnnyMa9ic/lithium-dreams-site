export const microcopy: string[] = [
  'Maintenance has already been notified.',
  'Please do not feed the groundskeeper.',
  'Extraterrestrial parking has moved behind the chapel.',
  'Bob says this is probably fine.',
  'Reflections may desynchronize during electrical storms.',
  'Authorized personnel and authorized cryptids only.',
  'Do not ask about the back room.',
  'No refunds after portal exposure.',
  'Please do not tap the glass.',
  'The groundskeeper is aware of your presence.',
  'This area is monitored. The monitor is friendly.',
  'Something has already been reported on your behalf.',
  'Temporary means something different here.',
  'The vending machine is not a vending machine.',
  'Please remain on the path. The path appreciates it.',
  'Cryptid sightings should be reported to the front desk.',
  'The fog has been here longer than the attraction.',
  'Your ticket is valid. Your reasons are your own.',
  'The manager is in. The manager is always in.',
  'Coffee is available. Coffee has been available for some time.',
  'Exit signs indicate exits. Other signs indicate other things.',
  'Please keep your hands inside the signal at all times.',
  'The lights have been adjusted for your comfort.',
  'Electrical storms are a courtesy, not a warning.',
];

export function randomMicrocopy(): string {
  return microcopy[Math.floor(Math.random() * microcopy.length)];
}
