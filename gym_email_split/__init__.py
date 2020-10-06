from gym.envs.registration import register

register(
    id='email_split-v0',
    entry_point='gym_email_split.envs:Email_SplitEnv',
)
register(
    id='email_split-extrahard-v0',
    entry_point='gym_email_split.envs:Email_SplitExtraHardEnv',
)